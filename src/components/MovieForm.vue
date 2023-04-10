<template>
    <div class="movie-form">
        <div v-if="error" class="error alert alert-danger">Invalid information</div>
        <div class="alert alert-success" role="alert" v-if="message">{{ message }}</div>
        <form 
            @submit.prevent="saveMovie" 
            method="post" 
            enctype="multipart/form-data"
            id="MovieForm"
            ref="MovieForm" >

            <div class="row">
                <div class="form-field col">
                    <label for="title">Title</label>
                    <input 
                        type="text" 
                        name="title" 
                        id="title" 
                        v-model="title"
                        required
                    />
                </div>
            </div>  
            <div class="form-field">
                <label for="description">Description</label>
                <textarea 
                    name="description" 
                    id="description" 
                    v-model="description" 
                    cols="30" 
                    rows="10"
                    required
                ></textarea>
            </div>
            <div class="form-field">
                <label for="poster">Upload poster</label>
                <input 
                    type="file" 
                    name="poster" 
                    id="poster" 
                    ref="poster" 
                    accept="image/png, image/jpg, image/jpeg"
                    @change="handleFileUpload"
                    required
                />
            </div>

            <button type="submit" class="submit-btn">Save Movie</button>
        </form>
    </div>
</template>

<script setup> </script>


<style scoped>
</style>