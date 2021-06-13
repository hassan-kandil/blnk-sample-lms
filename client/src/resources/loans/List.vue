<template>
  <base-material-card :icon="resource.icon" :title="title">
    <va-list :filters="filters">
      <va-data-table :fields="fields">
        <template v-slot:[`field.loan_type`]="{ value }">
          <v-chip :color="getLoanTypeColor(value.value)" dark>
            {{ value.text }}
          </v-chip>
        </template>
      </va-data-table>
    </va-list>
  </base-material-card>
</template>

<script>
export default {
  props: ["resource", "title"],
  data() {
    return {
      filters: [
        "duration",
        { source: "min_value", type: "number" },
        { source: "max_value", type: "number" },

        { source: "loan_type", type: "select" },
      ],
      fields: [
        {
          source: "id",
          label: "Name",
        },
        {
          source: "loan_type",
          labelKey: "loan_type",
          type: "select",
        },
        {
          source: "duration",
          label: "Duration (years)",
          sortable: true,
        },
        {
          source: "annual_interest",
          label: "Annual Interest (%)",
          type: "number",
          sortable: true,
          attributes: {
            format: "percent",
          },
        },
        {
          source: "min_value",
          label: "Min Value (EGP)",
          type: "number",
          sortable: true,
          attributes: {
            format: "currency",
          },
        },
        {
          source: "max_value",
          label: "Max Value (EGP)",
          type: "number",
          sortable: true,
          attributes: {
            format: "currency",
          },
        },

        {
          source: "created_at",
          type: "date",
          sortable: true,
        },
      ],
    };
  },
  methods: {
    getLoanTypeColor(loan_type) {
      if (loan_type === "personal") return "grey";
      else if (loan_type === "mortgage") return "orange";
      else if (loan_type === "car finance") return "red";
      else if (loan_type === "travel") return "blue";
      else return "green";
    },
  },
};
</script>
