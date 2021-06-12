<template>
    <va-edit-layout>
        <loan-fund-applications-form :id="id" :title="title" :item="item"></loan-fund-applications-form>
    </va-edit-layout>
</template>

<script>
export default {
    props: ["id", "title", "item"],
};
</script>