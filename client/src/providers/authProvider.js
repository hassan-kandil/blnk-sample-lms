/* eslint-disable */

import {
    LOGIN,
    CHECK_AUTH,
    CHECK_ERROR,
    GET_NAME,
    GET_EMAIL,
    LOGOUT,
    GET_PERMISSIONS,
} from "vuetify-admin/src/providers/auth/actions";

import FetchHydra from "vuetify-admin/src/providers/utils/fetchHydra";


export default (httpClient, params = {}) => {


    if (typeof httpClient === "string") {
        httpClient = new FetchHydra(httpClient);
    }

    params = {
        routes: {
            login: "api/auth/login",
            logout: "api/auth/logout",
            refresh: "api/auth/refresh",
            user: "api/auth/me",
        },
        storageKey: "jwt_token_lms_blnk",
        refreshStorageKey: "jwt_refresh_lms_blnk",
        getToken: (r) => r.access,
        getRefreshToken: (r) => r.refresh,
        getCredentials: ({ username, password }) => {
            return {
                username: username,
                password: password,
            };
        },
        getName: (u) => u.name,
        getEmail: (u) => u.email,
        getPermissions: (u) => u.groups,
        ...params,
    };

    let {
        routes,
        storageKey,
        refreshStorageKey,
        getCredentials,
        getName,
        getEmail,
        getPermissions,
        getToken,
        getRefreshToken
    } = params;

    return {
        [LOGIN]: async ({ username, password }) => {
            let response = await httpClient.post(
                routes.login,
                getCredentials({ username, password }),
            {
                headers: {
                    "X-Requested-With": "XMLHttpRequest",
                    "Authorization" : ""
                }
            }
            );

            if (response.status < 200 || response.status >= 300) {
                throw new Error(response.statusText);
            }

            localStorage.setItem(storageKey, getToken(response.data));
            localStorage.setItem(refreshStorageKey, getRefreshToken(response.data));


            httpClient.defaults.headers.common['Authorization'] = "Bearer " + localStorage.getItem(storageKey)



            return Promise.resolve();
        },
        [LOGOUT]: async () => {
            if (routes.logout) {
                await httpClient.post(routes.logout, {
                    refresh: localStorage.getItem(refreshStorageKey)
                },
                    {
                        headers: {
                            "X-Requested-With": "XMLHttpRequest",
                            "Authorization": ""
                        },


                    },
                );
            }

            localStorage.removeItem(storageKey);
            localStorage.removeItem(refreshStorageKey);
            return Promise.resolve();
        },
        [CHECK_AUTH]: async () => {

            if (localStorage.getItem(storageKey)) {

                if (localStorage.getItem(refreshStorageKey)) {

                    let response_refresh = await httpClient.get(

                        routes.refresh,
                        {
                            headers: {
                                "Refresh": localStorage.getItem(refreshStorageKey),
                                "Authorization" : "Bearer " + localStorage.getItem(storageKey)
                            }
                        });
                    localStorage.setItem(storageKey, getToken(response_refresh.data));
                    // console.log("REFRESH IS HERREEE");
                    // console.log(localStorage.getItem(storageKey))
                    httpClient.defaults.headers.common['Authorization'] = "Bearer " + localStorage.getItem(storageKey)

                }

                let response = await httpClient.get(routes.user, {
                    headers: {
                        "X-Requested-With": "XMLHttpRequest",
                        "Authorization": "Bearer " + localStorage.getItem(storageKey)
                    }
                });

                if (response.status < 200 || response.status >= 300) {
                    throw new Error(response.statusText);
                }

                return Promise.resolve({
                    data: response.data,
                });
            }

            return Promise.reject();
        },
        [CHECK_ERROR]: ({ status }) => {
            if (status === 401 || status === 403) {
                localStorage.removeItem(storageKey);
                localStorage.removeItem(refreshStorageKey);
                return Promise.reject();
            }
            return Promise.resolve();
        },
        [GET_NAME]: (user) => getName(user),
        [GET_EMAIL]: (user) => getEmail(user),
        [GET_PERMISSIONS]: (user) => getPermissions(user),
    };
};