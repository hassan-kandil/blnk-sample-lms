<template>
  <v-form ref="form" @submit.prevent="validate">
    <div class="text-right text-body-2">
      <router-link :to="{ name: 'register' }">
        {{ $t("auth.register") }} &gt;
      </router-link>
    </div>

    <v-text-field
      :label="$t('auth.username')"
      prepend-icon="mdi-account"
      v-model="form.username"
      required
      :error-messages="errorMessages.username"
    ></v-text-field>

    <div class="text-right text-body-2">
      <router-link :to="{ name: 'forgot_password' }">
        {{ $t("auth.forgot_password") }} &gt;
      </router-link>
    </div>

    <v-text-field
      :label="$t('auth.password')"
      prepend-icon="mdi-lock"
      type="password"
      v-model="form.password"
      required
      :error-messages="errorMessages.password"
    ></v-text-field>


    <div class="text-center">
      <v-btn
        :loading="loading"
        color="primary"
        large
        type="submit"
        text
        rounded
        >{{ $t("auth.sign_in") }}</v-btn
      >
    </div>
  </v-form>
</template>

<script>
import { mapActions } from "vuex";

export default {
  data() {
    return {
      form: {
        username: null,
        password: null,
      },
      errorMessages: {},
      loading: false,
    };
  },
  methods: {
    ...mapActions({
      login: "auth/login",
    }),
    async validate() {
      if (this.$refs.form.validate()) {
        this.loading = true;

        try {
          await this.login(this.form);
        } catch (e) {
          if (e.errors["password"] || e.errors["username"]) {
            this.errorMessages = e.errors;
            return;
          }

          this.errorMessages = { username: e.errors["non_field_errors"] };
        } finally {
          this.loading = false;
          // router.push(router.currentRoute.query.to || '/')

        }
      }
    },
  },
};
</script>

<style scoped>
#login-page {
  background-color: var(--v-primary-lighten5);
}
</style>
