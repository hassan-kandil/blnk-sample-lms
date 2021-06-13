<template>
  <va-show-layout>
    <va-show :id="id" :item="item">
      <v-row justify="center">
        <v-col lg="8">
          <base-material-tabs-card
            :tabs="[
              { id: 'attributes', label: 'attributes', icon: 'mdi-eye' },
              {
                id: 'amortization',
                label: 'amortization',
                icon: 'mdi-file-chart-outline',
              },
            ]"
          >
            <template v-slot:attributes>
              <v-row>
                <v-col>
                  <va-field source="id" label="Application ID"></va-field>
                </v-col>
                <v-col>
                  <va-field
                    source="submitted_by"
                    label="Submitted By"
                  ></va-field>
                </v-col>
                <v-col>
                  <va-field source="company" label="Company"></va-field>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <va-field
                    source="loanfund_id"
                    label="Loan Fund"
                    type="reference"
                    reference="loan-funds"
                    chip
                    color="blue"
                  ></va-field>
                </v-col>
                <v-col>
                  <va-field
                    source="amount"
                    type="number"
                    format="currency"
                  ></va-field>
                </v-col>
                <v-col>
                  <va-field source="status" type="select"></va-field>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <va-field
                    source="created_at"
                    type="date"
                    format="short"
                  ></va-field>
                </v-col>
                <v-col>
                  <va-field
                    source="start_date"
                    type="date"
                    format="short"
                  ></va-field>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <va-field
                    source="installment"
                    label="Installment Amount (EGP)"
                    type="number"
                    fomat="currency"
                  ></va-field>
                </v-col>
              </v-row>
              <va-field source="notes"></va-field>
            </template>
            <template v-slot:amortization>
              <va-list
                resource="amortizations"
                disable-query-string
                :items-per-page="10"
                :filter="{
                  loanfund_application: id,
                }"
                disable-create
                disableGlobalSearch
              >
                <va-data-table :fields="fields"> </va-data-table>
              </va-list>
            </template>
          </base-material-tabs-card>
        </v-col>
      </v-row>
    </va-show>
  </va-show-layout>
</template>

<script>
export default {
  props: ["id", "title", "item"],
  data() {
    return {
      fields: [
        "payment_no",
        {
          source: "date",
          type: "date",
          label: "Date",
          sortable: true,
          attributes: {
            format: "short",
          },
        },
        {
          source: "payment",
          type: "number",
          label: "Payment Amount",
          sortable: true,
          attributes: {
            format: "currency",
          },
        },
        {
          source: "interest",
          label: "Interest",
          type: "number",
          sortable: true,
          attributes: {
            format: "currency",
          },
        },
        {
          source: "principal",
          label: "Principal",
          type: "number",
          sortable: true,
          attributes: {
            format: "currency",
          },
        },
        {
          source: "balance",
          label: "Ending Balance",
          type: "number",
          sortable: true,
          attributes: {
            format: "currency",
          },
        },
      ],
    };
  },
};
</script>