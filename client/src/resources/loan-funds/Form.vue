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
            <v-row>
              <va-text-input
                source="id"
                label="Name*"
                required
              ></va-text-input>
            </v-row>
            <v-row>
              <va-text-input source="description" multiline></va-text-input>
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
          </v-card-text>
          <va-save-button></va-save-button>
        </base-material-card>
      </v-col>
    </v-row>
  </va-form>
</template>

<script>
export default {
  props: ["id","title", "item"],
};
</script>
