<template>
    <va-edit-layout>
        <loan-funds-form :id="id" :title="title" :item="item"></loan-funds-form>
    </va-edit-layout>
</template>

<script>
export default {
    props: ["id", "title", "item"],
    methods: {
        editLoan(loan){
            console.log('emitting edit loan', loan)
        }
    }
};
</script>