var vm = new Vue({
    el: '#app',
    data() {
            return {
                info: null
            }
        },
        mounted() {
            var getURL = "sample/sample.json"
            axios.get(getURL)
                .then(response => (this.info = response.data))
        },
    filters: {
        title_tranc: function (value) {
            len = 10
            end = "..."
            if (value.length > len){
                return value.substring(0, len) + end;
            }
            return value
        },
        text_tranc: function (value) {
            len = 100
            end = "..."
            if (value.length > len) {
                return value.substring(0, len) + end;
            }
            return value
        }
    }
})

