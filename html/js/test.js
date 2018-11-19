new Vue({
    el: '#app',
    data() {
        return {
            info: null
        }
    },
    mounted() {
        axios
            .get('https://6a3r6dm5pk.execute-api.us-east-1.amazonaws.com/develop/update')
            .then(response => (this.info = response.data))
    },
    filters: {
            title_tranc: function (value) {
                len = 10
                end = "..."
                if (value.length > len) {
                    return value.substring(0, len) + end;
                }
                return value
            },
    }
})


