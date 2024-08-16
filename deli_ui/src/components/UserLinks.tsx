"use client";
import React from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import Cookies from "js-cookie";
const UserLinks = () => {
  const router = useRouter();
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  useEffect(() => {
    const token = Cookies.get("access_token");
    setIsLoggedIn(!!token);
    console.log(token);
  }, []);

  const handLeLogut = () => {
    Cookies.remove("access_token");
    setIsLoggedIn(false);
    router.push("/login");
  };

  return (
    <div>
      {!isLoggedIn ? (
        <Link href="/login">Login</Link>
      ) : (
        <>
          <Link href="/orders">Orders</Link>
          <span className="ml-4 cursor-pointer" onClick={handLeLogut}>
            Logout
          </span>
        </>
      )}
    </div>
  );
};

export default UserLinks;
