<template>
    <div class="form-container">
        <h1>Upload Form</h1>
        <div v-if="success" class="alert alert-success" role="alert">
            <p>Movie Successfully added</p>
        </div>
        <div v-if="errors.length" class="alert alert-danger" role="alert">
            <ul class="error">
                <li  v-for="error in errors" :key="errors.indexOf(error)">{{ error }}</li>
            </ul>
        </div>
        <form @submit.prevent="saveMovie" method="post" enctype="multipart/form-data" id="MovieForm" ref="MovieForm" >

            
                <div class="form-field">
                    <label for="title" class="form-label">Movie Title</label>
                    <input type="text" name="title" class="form-control" />
                    
                </div>
                <div class="form-field">
                    <label for="description" class="form-label">Description</label>
                    <textarea name="description" id="description" cols="30" rows="10"></textarea>
                </div>
              
            <div class="form-field">
                <label for="poster">Upload Poster</label>
                <input type="file" name="poster" id="poster" ref="poster" accept="image/png, image/jpg, image/jpeg"
                    @change="handleFileUpload"
                    required
                />
            </div>

            <button type="submit">Save Movie</button>
        </form>
    </div>
</template>

<script>


export default{
    name: 'MovieForm',
    data(){
        return{
            csrf_token: '',
            errors: [],
            success:false
        }
    },
    created(){
        this.getCsrfToken();
    },
    methods:{
        saveMovie(){
            let MovieForm = document.getElementById('MovieForm');
            let form_data = new FormData(MovieForm);
            let self = this
            fetch("/api/v1/movies", {
                method: 'POST',
                body: form_data,
                headers:{
                    'X-CSRFToken': this.csrf_token
                }
            })
            .then(function (response) {
                return response.json();
            })
            .then(function (data) {
                // display a success message
                console.log(data);
                if('errors' in data){
                    self.errors=[...data.errors]
                    self.success = false
                } else {
                    self.errors=[]
                    self.errors= true
                }
            })
            .catch(function (error) {
                console.log(error);
            });
        },

        getCsrfToken() {
            fetch('/api/v1/csrf-token')
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            csrf_token.value = data.csrf_token;
        })
        }
    }
}


</script>


<style scoped>
.form-container{
    padding: 1rem 4rem;
}
.form-field{
    margin: 1rem 0;
}
.form-field input, .form-field textarea{
    display: block;
    border: 1px solid #cccccc;
    border-radius: 6px;
}
#description{
    width: 50%;
}
button{
    padding: 10px 2rem;
    border: none;
    background: #14b8a7;
    border-radius: 6px;
    color: #fff;
}

</style>