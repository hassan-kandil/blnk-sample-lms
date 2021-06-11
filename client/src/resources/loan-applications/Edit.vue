<template>
    <va-edit-layout>
        <loan-applications-form :id="id" :title="title" :item="item"></loan-applications-form>
    </va-edit-layout>
</template>

<script>
export default {
    props: ["id", "title", "item"],
};
</script>