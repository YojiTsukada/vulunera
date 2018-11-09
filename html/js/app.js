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
        }
    })
