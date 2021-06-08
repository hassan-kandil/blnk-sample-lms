<template>
  <base-material-card :icon="resource.icon" :title="title">
    <va-list>
      <va-data-table :fields="fields"> </va-data-table>
    </va-list>
  </base-material-card>
</template>

<script>
export default {
  props: ["resource", "title"],
  data() {
    return {
      fields: [
        "name",
        {
          source: "loan_type",
          labelKey: "loan_type",
          type: "chip",
        },
        {
          source: "duration",
          label: "Duration (years)",
        },
        {
          source: "annual_interest",
          label: "Annual Interest (%)",
          type: "number",
          sortable: true,
          attributes: {
            format: "percent",
          }
        },
        {
          source: "created_at",
          type: "date",
        },
      ],
    };
  },
};
</script>
