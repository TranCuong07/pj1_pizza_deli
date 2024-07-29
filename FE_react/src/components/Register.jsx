import { useState } from "react";
import FormInput from "./FormInput";

const Register = () =>{
    const [values, setValues] = useState({
        username: "",
        email: "",
        birthday: "",
        password: "",
        confirmPassword: "",
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
            name: "email",
            type: "email",
            placeholder:"email",
            errorMessage:
            "It should be a valid email address!",
            label: "email",
            require: true,
        },
        {
            id:3,
            name: "birthday",
            type: "date",
            placeholder:"birthday",
            label: "birthday",
        },
        {
            id:4,
            name: "password",
            type: "password",
            placeholder:"password",
            errorMessage:
            "Password should be 8-20 characters and include at least 1 letter, 1 number and 1 special character!",
            label: "password",
            require: true,
        },
        {
            id:5,
            name: "confirmPassword",
            type: "password",
            placeholder:"confirmPassword",
            errorMessage: "Passwords don't match!",
            label: "Confirm Password",
            pattern: values.password,
            required: true,
        },
    ]


    const handleSubmit = (e) =>{
        e.preventDefault();
    };

    const onChange = (e) => {
        setValues({...values, [e.target.name]: e.target.value});
    };
    console.log(values);
return <div className="app"> 
    <form onSubmit={handleSubmit}>
    <h1>Register</h1>
        {input.map((input) => (
        <FormInput
            key={input.id}{...input}
            value={values[input.name]}
            onChange={onChange}
        />
    ))}
        <button>Submit</button>
    </form>
    </div>;
};
export default Register;