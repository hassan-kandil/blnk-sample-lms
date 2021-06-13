<template>
  <div>
    <v-container class="full-height" fluid>
      <v-row dense>
        <v-col cols="12" lg="12">
          <base-material-chart-card
            :data="emailsSubscriptionChart.data"
            :options="emailsSubscriptionChart.options"
            :responsive-options="emailsSubscriptionChart.responsiveOptions"
            color="#E91E63"
            hover-reveal
            type="Bar"
          >
            <template v-slot:reveal-actions>
              <v-tooltip bottom>
                <template v-slot:activator="{ attrs, on }">
                  <v-btn v-bind="attrs" color="info" icon v-on="on">
                    <v-icon color="info"> mdi-refresh </v-icon>
                  </v-btn>
                </template>

                <span>Refresh</span>
              </v-tooltip>

              <v-tooltip bottom>
                <template v-slot:activator="{ attrs, on }">
                  <v-btn v-bind="attrs" light icon v-on="on">
                    <v-icon>mdi-pencil</v-icon>
                  </v-btn>
                </template>

                <span>Change Date</span>
              </v-tooltip>
            </template>

            <h4 class="card-title font-weight-light mt-2 ml-2">
              Forecasted Monthly Profit
            </h4>
          </base-material-chart-card>
        </v-col>
      </v-row>
    </v-container>
    <v-row>
      <v-col cols="12" sm="9" lg="6">
        <base-material-stats-card
          color="info"
          icon="mdi-text-box-multiple"
          title="Upcoming Month Total Loan Installments"
          :value="total_loan_installments"
        />
      </v-col>

      <v-col cols="12" sm="9" lg="6">
        <base-material-stats-card
          color="orange"
          icon="mdi-book-plus-multiple"
          title="Upcoming Month Total Loan Fund Installments"
          :value="total_loanfund_installments"
        />
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12" sm="9" lg="6">
        <base-material-stats-card
          color="red"
          icon="mdi-account-cash"
          title="Total Loans Given"
          :value="total_loans"
        />
      </v-col>

      <v-col cols="12" sm="9" lg="6">
        <base-material-stats-card
          color="success"
          icon="mdi-cash-plus"
          title="Total Funds Received"
          :value="total_funds"
        />
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      dailySalesChart: {
        data: {
          labels: ["M", "T", "W", "T", "F", "S", "S"],
          series: [[12, 17, 7, 17, 23, 18, 38]],
        },
        options: {
          lineSmooth: this.$chartist.Interpolation.cardinal({
            tension: 0,
          }),
          low: 0,
          high: 50, // creative tim: we recommend you to set the high sa the biggest value + something for a better look
          chartPadding: {
            top: 0,
            right: 0,
            bottom: 0,
            left: 10,
          },
        },
      },
      dataCompletedTasksChart: {
        data: {
          labels: ["12am", "3pm", "6pm", "9pm", "12pm", "3am", "6am", "9am"],
          series: [[230, 750, 450, 300, 280, 240, 200, 190]],
        },
        options: {
          lineSmooth: this.$chartist.Interpolation.cardinal({
            tension: 0,
          }),
          low: 0,
          high: 1000, // creative tim: we recommend you to set the high sa the biggest value + something for a better look
          chartPadding: {
            top: 0,
            right: 0,
            bottom: 0,
            left: 0,
          },
        },
      },
      emailsSubscriptionChart: {
        data: {
          labels: [
            "Ju",
            "Jul",
            "Au",
            "Se",
            "Oc",
            "No",
            "De",
            "Ja",
            "Fe",
            "Ma",
            "Ap",
            "Mai",
          ],
          series: [
            [542, 443, 320, 780, 553, 453, 326, 434, 568, 610, 756, 895],
          ],
        },
        options: {
          axisX: {
            showGrid: true,
          },
          low: 0,
          high: 10000,
          chartPadding: {
            top: 0,
            right: 5,
            bottom: 0,
            left: 0,
          },
        },
        responsiveOptions: [
          [
            "screen and (max-width: 640px)",
            {
              seriesBarDistance: 5,
              axisX: {
                labelInterpolationFnc: function (value) {
                  return value[0];
                },
              },
            },
          ],
        ],
      },
      headers: [
        {
          sortable: false,
          text: "ID",
          value: "id",
        },
        {
          sortable: false,
          text: "Name",
          value: "name",
        },
        {
          sortable: false,
          text: "Salary",
          value: "salary",
          align: "right",
        },
        {
          sortable: false,
          text: "Country",
          value: "country",
          align: "right",
        },
        {
          sortable: false,
          text: "City",
          value: "city",
          align: "right",
        },
      ],
      items: [
        {
          id: 1,
          name: "Dakota Rice",
          country: "Niger",
          city: "Oud-Tunrhout",
          salary: "$35,738",
        },
        {
          id: 2,
          name: "Minerva Hooper",
          country: "Curaçao",
          city: "Sinaai-Waas",
          salary: "$23,738",
        },
        {
          id: 3,
          name: "Sage Rodriguez",
          country: "Netherlands",
          city: "Overland Park",
          salary: "$56,142",
        },
        {
          id: 4,
          name: "Philip Chanley",
          country: "Korea, South",
          city: "Gloucester",
          salary: "$38,735",
        },
        {
          id: 5,
          name: "Doris Greene",
          country: "Malawi",
          city: "Feldkirchen in Kārnten",
          salary: "$63,542",
        },
      ],
      tabs: 0,
      tasks: {
        0: [
          {
            text: 'Sign contract for "What are conference organizers afraid of?"',
            value: true,
          },
          {
            text: "Lines From Great Russian Literature? Or E-mails From My Boss?",
            value: false,
          },
          {
            text: "Flooded: One year later, assessing what was lost and what was found when a ravaging rain swept through metro Detroit",
            value: false,
          },
          {
            text: "Create 4 Invisible User Experiences you Never Knew About",
            value: true,
          },
        ],
        1: [
          {
            text: "Flooded: One year later, assessing what was lost and what was found when a ravaging rain swept through metro Detroit",
            value: true,
          },
          {
            text: 'Sign contract for "What are conference organizers afraid of?"',
            value: false,
          },
        ],
        2: [
          {
            text: "Lines From Great Russian Literature? Or E-mails From My Boss?",
            value: false,
          },
          {
            text: "Flooded: One year later, assessing what was lost and what was found when a ravaging rain swept through metro Detroit",
            value: true,
          },
          {
            text: 'Sign contract for "What are conference organizers afraid of?"',
            value: true,
          },
        ],
      },
      list: {
        0: false,
        1: false,
        2: false,
      },
      total_loans: 0,
      total_funds: 0,
      total_loan_installments: 0,
      total_loanfund_installments: 0,
    };
  },

  methods: {
    complete(index) {
      this.list[index] = !this.list[index];
    },
  },
  async mounted() {
    try {
      let response = await this.$admin.http.get("api/profit-stats");
      let response_totals = await this.$admin.http.get("api/total-stats");

      this.$router.push("/");

      this.emailsSubscriptionChart.data.series = [response.data];
      this.total_loan_installments =
        response_totals.data.total_loan_installments;
      this.total_loanfund_installments =
        response_totals.data.total_loanfund_installments;

      this.total_loans = response_totals.data.total_loans;
      this.total_funds = response_totals.data.total_funds;
    } catch (e) {
      if (e.errors) {
        this.errorMessages = e.errors;
        return;
      }
      this.message = e.message;
    }
  },
};
</script>
