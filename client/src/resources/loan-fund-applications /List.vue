<template>
  <base-material-card :icon="resource.icon" :title="title">
    <va-list>
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
      fields: [
        "id",
        {
          source: "submitted_by",
          label: "Submitted By",
        },
        {
          source: "company",
          label: "Company",
        },
        {
          source: "loanfund.id",
          label: "Loan Fund Name",
          type: "reference",
          attributes: {
            text: "name",
            reference: "loan-funds",
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
          attributes : {
            format:"short"
          }
        },
        {
          source: "status",
          type: "select"
        },
      ],
    };
  },
  methods: {
      getStatusColor (status) {
        if (status === 'pending') return 'grey'
        else if (status === 'missing') return 'orange'
        else if (status === 'rejected') return 'red'
        else return 'green'
      },
    },
};
</script>
