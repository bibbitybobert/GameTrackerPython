<script lang="ts">
    import {enhance} from "$app/forms";
    import type {ActionData} from './$types';

    let {form}:{ form: ActionData} = $props();
</script>

<h1>Login</h1>
<form class="container" method="post" action="?/login" use:enhance>
    <div class="input">
        <label>
            Email
            <input name="email">
        </label>
    </div>
    <div class="input">
        <label>
            Password
            <input name="password" type="password">
        </label>
    </div>
    <div class="buttons">
    <button>Login</button>|<button formaction="?/register">Register</button>
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
    }

    .buttons button{
        text-align: center;
        margin-left: 15px;
        margin-right: 15px;
    }
</style>