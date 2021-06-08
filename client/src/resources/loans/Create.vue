<template>
    <va-create-layout>
        <loans-form :title="title" :item="item"></loans-form>
    </va-create-layout>
</template>

<script>
export default {
    props: ["title", "item"],
};
</script>