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
              </v-row>
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
                <v-col>
                  <va-field source="status" type="select"></va-field>
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
              <va-field source="notes"></va-field>
            </template>
            <template v-slot:amortization>
              <va-rich-text-field source="amortization"></va-rich-text-field>
            </template>
          </base-material-tabs-card>
        </v-col>
      </v-row>
    </va-show>
  </va-show-layout>
</template>

<script>
export default {
  props: ["title", "item"],
};
</script>