<template>
  <base-material-card :icon="resource.icon" :title="title">
    <va-list :filters="filters">
      <va-data-table :fields="fields">
        <template v-slot:[`field.status`]="{ value }">
          <v-chip :color="getStatusColor(value.value)" dark>
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
        {
          source: "profile.full_official_name",
          label: "Applicant Name"
        },
        {
          source: "loan.id",
          label: "Loan Name",
          type: "autocomplete",
          attributes: {
            optionText: "name",
            multiple: true,
            reference: "loans",
          },
        },
        { source: "status", type: "select" },
      ],
      fields: [
        "id",
        {
          source: "profile.full_official_name",
          labelKey: "Applicant Name",
        },
        {
          source: "loan.id",
          label: "Loan Name",
          type: "reference",
          attributes: {
            text: "name",
            reference: "loans",
            chip: true,
            color: "blue",
          },
        },
        {
          source: "amount",
          label: "Amount",
          type: "number",
          sortable: true,
          attributes: {
            format: "currency",
          },
        },
        {
          source: "created_at",
          type: "date",
          label: "Date",
          sortable: true,
        },
        {
          source: "status",
          type: "select",
        },
      ],
    };
  },
  methods: {
    getStatusColor(status) {
      if (status === "pending") return "grey";
      else if (status === "missing") return "orange";
      else if (status === "rejected") return "red";
      else return "green";
    },
  },
};
</script>
