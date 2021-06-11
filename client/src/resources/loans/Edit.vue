<template>
    <va-edit-layout>
        <loans-form @edit-loan = "editLoan" :id="id" :title="title" :item="item"></loans-form>
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