<template>
  <base-material-card :icon="resource.icon" :title="title">
    <va-list>
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
      fields: [
        {
          source: "id",
          label : "Name"
        },
        {
          source: "loan_type",
          labelKey: "loan_type",
          type: "select",
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
  methods: {
      getLoanTypeColor (loan_type) {
        if (loan_type === 'personal') return 'grey'
        else if (loan_type === 'mortgage') return 'orange'
        else if (loan_type === 'car finance') return 'red'
        else if (loan_type === 'travel') return 'blue'
        else return 'green'
      },
    }
};
</script>
