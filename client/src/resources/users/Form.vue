<template>
  <va-form :id="id" :item="item" disable-redirect @saved="$emit('saved')">
    <va-text-input source="first_name" required></va-text-input>
    <va-text-input source="last_name" required ></va-text-input>
    <va-text-input source="username" required></va-text-input>
    <va-text-input source="email" type="email" required></va-text-input>
    <va-password-input source="password" required></va-password-input>
    <va-password-input source="password_confirmation" required></va-password-input>
    <va-save-button></va-save-button>
  </va-form>
</template>

<script>
export default {
  props: ["id", "item"],
};
</script>
