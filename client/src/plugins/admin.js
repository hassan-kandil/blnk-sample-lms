import Vue from "vue";
import VuetifyAdmin from "vuetify-admin";

import "vuetify-admin/src/loader";

import dataProvider from "@/providers/dataProvider";
import authProvider from "@/providers/authProvider";


// import {
//   jwtAuthProvider,
// } from "vuetify-admin/src/providers";
import {
  en,
} from "vuetify-admin/src/locales";


import router from "@/router";
import routes from "@/router/admin";
import store from "@/store";
import i18n from "@/i18n";
import resources from "@/resources";
import axios from "axios";

/**
 * Load Admin UI components
 */
Vue.use(VuetifyAdmin);

/**
 * Axios instance
 */
const baseURL = process.env.VUE_APP_API_URL || "http://localhost:8000/";

const http = axios.create({
  baseURL,
  headers: {
    "X-Requested-With": "XMLHttpRequest"
    },
  
}
);


/**
 * Init admin
 */
export default new VuetifyAdmin({
  router,
  store,
  i18n,
  title: "blnk LMS",
  routes,
  locales: {
    en,
  },
  translations: [
    "en",
  ],
  authProvider: authProvider(http),
  dataProvider: dataProvider(http),
  resources,
  http,
  options: {
    dateFormat: "long",
  },
});
