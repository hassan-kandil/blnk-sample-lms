/* eslint-disable no-unused-vars */

export default (i18n, admin) => [
  {
    icon: "mdi-view-dashboard",
    text: i18n.t("menu.dashboard"),
    link: "/",
  },
  { divider: true },
  ...admin.getResourceLinks([
    "loans",
    "loan-funds",
    "users",

  ]),
];
