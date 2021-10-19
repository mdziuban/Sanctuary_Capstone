<template>
    <div class="logout">

    </div>
</template>

<script>
export default {
    created () {
        this.$store.dispatch('userLogout')
    }
}
</script>