<template>
    <va-create-layout>
        <loan-fund-applications-form :title="title" :item="item"></loan-fund-applications-form>
    </va-create-layout>
</template>

<script>
export default {
    props: ["title", "item"],
};
</script>