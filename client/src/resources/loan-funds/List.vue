<template>
  <base-material-card :icon="resource.icon" :title="title">
    <va-list :filters="filters">
      <va-data-table :fields="fields"> </va-data-table>
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
      ],
      fields: [
        {
          source: "id",
          label: "Name",
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
};
</script>
