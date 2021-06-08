<template>
    <va-create-layout>
        <loan-funds-form :title="title" :item="item"></loan-funds-form>
    </va-create-layout>
</template>

<script>
export default {
    props: ["title", "item"],
};
</script>