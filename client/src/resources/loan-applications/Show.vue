<template>
  <va-show-layout>
    <va-show :item="item">
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
                  <va-field
                    source="loan_id"
                    label="Loan"
                    type="reference"
                    reference="loans"
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
              </v-row>
              <v-row>
                <v-col>
                  <va-field source="status" type="select"></va-field>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <va-field
                    source="start_date"
                    label="Loan Start Date"
                    type="date"
                    format="short"
                  ></va-field>
                </v-col>
                <v-col>
                  <va-field
                    source="loan.installment_frequency"
                    label="Loan Installment Frequency"
                    type="select"
                  ></va-field>
                </v-col>
              </v-row>

              <v-row>
                <v-col>
                  <va-field
                    source="profile.full_official_name"
                    label="Full Legal Name"
                  ></va-field>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <va-field
                    source="profile.national_id"
                    label="National ID"
                  ></va-field>
                </v-col>
                <v-col>
                  <va-field
                    source="profile.birth_date"
                    label="Birth Date"
                    type="date"
                    format="short"
                  ></va-field>
                </v-col>
              </v-row>

              <v-row>
                <v-col>
                  <va-field
                    source="profile.gender"
                    label="Gender"
                    type="select"
                    chip
                  ></va-field>
                  <va-field
                    source="profile.mobile_no"
                    label="Mobile Number"
                  ></va-field>
                </v-col>
                <v-col>
                  <va-field
                    source="profile.profession"
                    label="Profession"
                  ></va-field>
                  <va-field
                    source="profile.employer"
                    label="Employer"
                  ></va-field>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <va-field
                    source="profile.monthly_income"
                    label="Monthy Income (EGP)"
                    type="number"
                    fomat="currency"
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
                  loan_application: id,
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