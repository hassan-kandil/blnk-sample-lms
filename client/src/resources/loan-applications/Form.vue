<template>
  <va-form :id="id" :item="item" disable-redirect @saved="$emit('saved')">
    <v-row justify="center">
      <v-col sm="6">
        <base-material-card>
          <template v-slot:heading>
            <div class="display-2">
              {{ title }}
            </div>
          </template>

          <v-card-text>
            <v-col>
              <v-row>
                <va-text-input
                  source="profile.full_official_name"
                  label="Full Legal Name*"
                  required
                ></va-text-input>
              </v-row>
            </v-col>
            <v-col>
              <v-row>
                <va-text-input
                  source="profile.national_id"
                  label="National ID*"
                  required
                ></va-text-input>
              </v-row>
            </v-col>
            <v-row>
              <v-col lg="8">
                <va-autocomplete-input
                  source="loan_id"
                  model="loan_id"
                  label="Loan Name*"
                  reference="loans"
                  required
                ></va-autocomplete-input>
              </v-col>
              <v-col>
                <va-number-input
                  source="amount"
                  label="Loan Amount (EGP)"
                  format="currency"
                  :step="1000"
                  :min="0"
                  :max="10000000000"
                ></va-number-input>
              </v-col>
            </v-row>
            <v-row>
              <v-col sm="6">
                <va-select-input
                  v-if="$admin.can(['admin'])"
                  source="status"
                  label="Application Status"
                ></va-select-input>
              </v-col>
              <v-col sm="6">
                <va-date-input
                  v-if="$admin.can(['admin'])"
                  label="Loan Start Date"
                  source="start_date"
                  format="short"
                ></va-date-input>
              </v-col>
            </v-row>
            <v-row>
              <v-col sm="6">
                <va-select-input
                  source="profile.gender"
                  label="Select Gender"
                ></va-select-input>
              </v-col>
              <v-col sm="6">
                <va-date-input
                  label="Birth Date"
                  source="profile.birth_date"
                  format="short"
                ></va-date-input>
              </v-col>
            </v-row>
            <v-row>
              <v-col lg="8">
                <va-text-input
                  source="profile.mobile_no"
                  label="Mobile Number"
                ></va-text-input>
              </v-col>
            </v-row>

            <v-row>
              <v-col>
                <va-text-input
                  source="profile.profession"
                  label="Profession"
                  required
                ></va-text-input>
              </v-col>
              <v-col>
                <va-text-input
                  source="profile.employer"
                  label="Employer"
                  required
                ></va-text-input>
              </v-col>
            </v-row>

            <v-col>
              <v-row>
                <va-number-input
                  source="profile.monthly_income"
                  label="Monthy Income (EGP)"
                  format="currency"
                  :step="1000"
                  :min="1000"
                  :max="100000000000000"
                ></va-number-input>
              </v-row>
            </v-col>
          </v-card-text>
          <va-save-button></va-save-button>
        </base-material-card>
      </v-col>
    </v-row>
  </va-form>
</template>

<script>
export default {
  props: ["id", "title", "item"],
};
</script>
