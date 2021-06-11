<template>
  <va-show-layout>
    <va-show :item="item">
      <v-row justify="center">
        <v-col lg="8">
          <base-material-tabs-card
            :tabs="[
              { id: 'attributes', label: 'attributes' ,icon: 'mdi-eye' },
              { id: 'amortization', label: 'amortization' ,icon: 'mdi-file-chart-outline' },
            ]"
          >
            <template v-slot:attributes>
              <v-row>
                <v-col>
                  <va-field source="id" label="Name"></va-field>
                </v-col>
                <v-col>
                  <va-field
                    source="loan_type"
                    labelKey="loan_type"
                    type="select"
                  ></va-field>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <va-field
                    source="min_value"
                    type="number"
                    format="currency"
                  ></va-field>
                  <va-field
                    source="max_value"
                    type="number"
                    format="currency"
                  ></va-field>
                </v-col>              
                <v-col>
                  <va-field
                    source="duration"
                    type="number"
                    label="Duration in years"
                  ></va-field>
                  <va-field
                    source="annual_interest"
                    type="number"
                    format="percent"
                  ></va-field>
                </v-col>
            </v-row>
            <v-row>
            <v-col>
                   <va-field
                    source="min_credit_score"
                    type="number"
                  ></va-field>
            </v-col>
            </v-row>
              <va-field source="description"></va-field>
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