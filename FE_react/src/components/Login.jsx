import { useState } from "react";
import FormInput from "./FormInput";

const Login = () =>{
    const [values, setValues] = useState({
        username: "",
        password: "",
    });

    const input = [
        {
            id:1,
            name: "username",
            type: "text",
            placeholder:"Username",
            errorMessage:
            "Username should be 3-16 characters and shouldn't include any special character!",
            label: "Username",
            pattern:"^[A-Za-z0-9]{3,16}$",
            require: true,
        },
        {
            id:2,
            name: "password",
            type: "password",
            placeholder:"password",
            errorMessage:
            "Password should be 8-20 characters and include at least 1 letter, 1 number and 1 special character!",
            label: "password",
            require: true,
        },
    ]


    const handleSubmit = async (e) =>{
        e.preventDefault();
        try{
            const response = await fetch("http://localhost:8000/auth/login",
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        
                    },
                    body: JSON.stringify(values)
                });

                if(response.ok){
                    const data = await response.json();
                    localStorage.setItem('token', data.acces_token) // luu token
                    //console.log(data);
                }else{
                    const errorData = await response.json();
                    throw new Error(errorData.detail);
                }          
            }       
        catch (error){
                console.error("Error:", error.message);
                alert(`Login failed: ${error.message}`);
            }
        };
    
    const onChange = (e) => {
        setValues({...values, [e.target.name]: e.target.value});
    };
    //console.log(values);
return <div className="app"> 
    <form onSubmit={handleSubmit}>
    <h1>Login</h1>
        {input.map((input) => (
        <FormInput
            key={input.id}{...input}
            value={values[input.name]}
            onChange={onChange}
        />
    ))}
        <button>Login</button>
    </form>
    </div>;
};
export default Login;