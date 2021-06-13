export default [
  {
    name : "loans",
    icon: "mdi-account-cash",
    routes: ["list", "edit", "create", "show"],
    permissions: [
      "admin",
      { name: "customer", actions: ["list", "show"] }
  ]
  },
  {
    name : "loan-funds",
    icon: "mdi-cash-plus",
    permissions: [
      "admin",
      { name: "provider", actions: ["list", "show"] }
  ]
  },
  {
    name: "users",
    icon: "mdi-account",
    routes: ["list"],
    permissions: ["admin"]
  },
  {
    name: "loan-applications",
    icon: "mdi-text-box-multiple",
    permissions: [
      "admin",
      { name: "customer", actions: ["list", "show", "create"] }
  ]
  },
  {
    name: "loan-fund-applications",
    icon: "mdi-book-plus-multiple",
    permissions: [
      "admin",
      { name: "provider", actions: ["list", "show", "create"] }
  ]
  },
  {
    name: "amortizations",
    icon: "mdi-text-box-multiple",
    routes: ["list"]
  }
];
