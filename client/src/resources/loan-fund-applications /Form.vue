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
                  source="submitted_by"
                  label="Employee Name*"
                  required
                ></va-text-input>
              </v-row>
            </v-col>
            <v-col>
              <v-row>
                <va-text-input
                  source="company"
                  label="Company*"
                  required
                ></va-text-input>
              </v-row>
            </v-col>
            <v-row>
              <v-col lg="8">
                <va-autocomplete-input
                  source="loanfund_id"
                  model="loanfund_id"
                  label="Loan Fund Name*"
                  reference="loan-funds"
                  required
                ></va-autocomplete-input>
              </v-col>
              <v-col>
                <va-number-input
                  source="amount"
                  label="Loan Fund Amount (EGP)"
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
                  label="Loan Fund Start Date"
                  source="start_date"
                  format="short"
                ></va-date-input>
              </v-col>
            </v-row>
      
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
