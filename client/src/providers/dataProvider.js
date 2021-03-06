/* eslint-disable no-unused-vars */

import {
  GET_LIST,
  GET_MANY,
  GET_TREE,
  GET_NODES,
  GET_ONE,
  CREATE,
  UPDATE,
  UPDATE_MANY,
  DELETE,
  DELETE_MANY,
  MOVE_NODE,
} from "vuetify-admin/src/providers/data/actions";

import objectToFormData from "vuetify-admin/src/providers/utils/objectToFormData";
import qs from "qs";

export default (axios, baseURL = "/api") => {
  /**
   * Add axios interceptors
   */


  axios.interceptors.request.use((config) => {
    if (config.locale) {
      config.headers.locale = config.locale;
    }
    return config;
  });

  axios.interceptors.response.use(
    (response) => {
      return response;
    },
    ({ message, response }) => {
      if (response) {


        let { status, statusText, data } = response;

        return Promise.reject({
          status,
          message: statusText,
          ...data,
        });
      }

      return Promise.reject({
        message,
      });
    }
  );

  const getResponse = (Promise) => Promise.then((data) => data);

  return {
    [GET_LIST]: async (resource, params) => {
      const { fields, include, pagination, sort, filter } = params;


      if (filter && filter.q) {
        filter.id = filter.q
        delete filter.q
      }


      let query = {
        fields,
        include,
        ...pagination,
      };

      for (var key in filter) {
        query[key] = filter[key]

      }




      if (sort && sort.length) {
        query.ordering = sort.map((item) => {
          let { by, desc } = item;

          if (desc) {
            return `-${by}`;
          }
          return by;
        });
        query.ordering = query.ordering.toString()
      }
      console.log(query.sort)

      console.log(query)

      return getResponse(
        axios.get(
          `${baseURL}/${resource}?${qs.stringify(query, {
            arrayFormat: "comma",
          })}`,
          query
        )
      ).then(({ data, meta }) => ({
        data: data.results ? data.results : data,
        total: data.count,
      }));
    },
    [GET_MANY]: (resource, params) => {
      const { fields, include } = params;

      let query = {
        fields,
        include,
        filter: {
          id: params.ids,
        },
      };

      return getResponse(
        axios.get(
          `${baseURL}/${resource}?${qs.stringify(query, {
            arrayFormat: "comma",
          })}`,
          { locale: params.locale }
        )
      );
    },
    [GET_TREE]: (resource, params) =>
      getResponse(
        axios.get(
          `${baseURL}/${resource}/tree?${qs.stringify(
            { filter: params.filter },
            { arrayFormat: "comma" }
          )}`,
          { locale: params.locale }
        )
      ),
    [GET_NODES]: (resource, params) =>
      getResponse(
        axios.get(
          `${baseURL}/${resource}/nodes/${params.parent ? params.parent.id : ""
          }?${qs.stringify(
            { filter: params.filter },
            { arrayFormat: "comma" }
          )}`,
          { locale: params.locale }
        )
      ),
    [GET_ONE]: (resource, params) =>
      getResponse(
        axios.get(`${baseURL}/${resource}/${params.id}`, {
          locale: params.locale,
        })
      ),
    [CREATE]: (resource, params) => {
      // let data = objectToFormData(params.data);
      return getResponse(
        axios.post(`${baseURL}/${resource}`, params.data, { locale: params.locale })
      );
    },
    [UPDATE]: (resource, params) => {

      // let data = objectToFormData(params.data);
      // data.append("_method", "PUT");


      return getResponse(
        axios.put(`${baseURL}/${resource}/${params.id}`, params.data, {
          locale: params.locale,
        })
      );
    },
    [UPDATE_MANY]: (resource, params) =>
      Promise.all(
        params.ids.map((id) =>
          axios.patch(`${baseURL}/${resource}/${id}`, params.data, {
            locale: params.locale,
          })
        )
      ).then(() => Promise.resolve()),
    [DELETE]: (resource, params) =>
      getResponse(axios.delete(`${baseURL}/${resource}/${params.id}`)),
    [DELETE_MANY]: (resource, params) =>
      Promise.all(
        params.ids.map((id) => axios.delete(`${baseURL}/${resource}/${id}`))
      ).then(() => Promise.resolve()),
    [MOVE_NODE]: (resource, params) =>
      getResponse(
        axios.patch(`${baseURL}/${resource}/${params.source.id}/move`, {
          parent_id: params.destination ? params.destination.id : null,
          position: params.position,
        })
      ),
  };
};