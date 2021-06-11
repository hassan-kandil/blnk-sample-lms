<template>
  <va-form :id="id" :item="item" disable-redirect @submit="onSubmit" @saved="$emit('saved')">
    <v-row justify="center">
      <v-col sm="6">
        <base-material-card>
          <template v-slot:heading>
            <div class="display-2">
              {{ title }}
            </div>
          </template>

          <v-card-text>
            <v-row>
              <va-text-input source="id" label="Name*" required></va-text-input>
            </v-row>
            <v-row>
              <va-text-input source="description" multiline></va-text-input>
            </v-row>
            <v-row>
              <va-select-input
                source="loan_type"
                label="Select Loan Type*"
                chip
                required
              ></va-select-input>
            </v-row>
            <v-row>
              <v-col sm="6">
                <va-number-input
                  source="duration"
                  label="Duration (years)*"
                  :step="1"
                  :min="1"
                  :max="99"
                  required
                ></va-number-input>
              </v-col>
              <v-col sm="6">
                <va-number-input
                  source="annual_interest"
                  label="Annual Interest Rate (%)*"
                  :step="0.25"
                  :min="1"
                  :max="100"
                  required
                ></va-number-input>
              </v-col>
            </v-row>
            <v-row>
              <v-col sm="6">
                <va-number-input
                  source="min_value"
                  label="Minimum Amount (EGP)"
                  format="currency"
                  :step="1000"
                  :min="0"
                  :max="100000000000000"
                ></va-number-input>
              </v-col>
              <v-col sm="6">
                <va-number-input
                  source="max_value"
                  label="Maximum Amount (EGP)"
                  format="currency"
                  :step="1000"
                  :min="1000"
                  :max="1000000000000000000000"
                ></va-number-input>
              </v-col>
            </v-row>
            <v-row>
              <va-number-input
                source="min_credit_score"
                label="Mimimum Credit Score"
                :step="50"
                :min="400"
                :max="850"
              ></va-number-input>
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
  methods: {
    onSubmit() {
      console.log("SUBMITTING")
      const loan = {
        id: this.id,
        description: this.description,
        min_value: this.min_value,
        max_value: this.max_value,
        duration: this.duration,
        annual_interest: this.annual_interest,
        min_credit_score: this.min_credit_score,
        loan_type: this.loan_type,
      };
      
      this.$emit("edit-loan", loan);
    },
  },
};
</script>
