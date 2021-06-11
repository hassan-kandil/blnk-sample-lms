<template>
    <va-create-layout>
        <loan-applications-form :title="title" :item="item"></loan-applications-form>
    </va-create-layout>
</template>

<script>
export default {
    props: ["title", "item"],
};
</script>