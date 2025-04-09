<script lang="ts">
    import {enhance} from "$app/forms";
    import type {ActionData} from './$types';

    let {form}:{ form: ActionData} = $props();
</script>

<h1>Register</h1>
<form class="container" method="post" action="?/register" use:enhance>
    <div class="input" id="NameInput">
        <div class="nameBlock">
            <div><label for="fName">First Name</label></div>
        <input name="fName">
        </div>
        <div id="spacer"/>
        <div class="nameBlock">
            <div><label for="lName">Last Name</label></div>
        <input name="lName">
        </div>
    </div>
    <div class="input">
        <div><label for="email">Email</label></div>
        <input name="email">
    </div>
    <div class="input">
        <div><label for="password">Password</label></div>
        <input name="password" type="password">
    </div>
    <div class="input">
        <div><label for="confirmPassword">Confirm Password</label></div>
        <input name="confirmPassword" type="password">
    </div>
    <div class="buttons">
    <button>Register</button>
    </div>
</form>

<style>
    h1{
        font-size: 2.4rem;
        text-align: center;
        font-weight: 400;
    }

    .container{
        display:flex;
        flex-direction: column;
        justify-content: center;
    }

    .input, .buttons{
        align-self: center;
        margin: 5px;
        width: 50%;
    }

    label{
        width: 100%;
    }

    .input input{
        width: 100%;
    }

    .nameBlock {
        width: 49%;
    }

    #NameInput{
        display: inline-flex;
        flex-direction: row;
    }

    #spacer{
        width: 2%;
    }

    .buttons button{
        text-align: center;
        width: 100%;
        align-self: center;
        background: red;

    }

</style>