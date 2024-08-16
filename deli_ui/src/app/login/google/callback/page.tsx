import axios from "axios";
import { useRouter } from "next/router";
import React, { useEffect } from "react";

const GoogleCallback = () => {
  const router = useRouter();
  const { code } = router.query;

  useEffect(() => {
    const fetchTokens = async () => {
      if (code) {
        try {
          const reponse = await axios.get(
            `http://localhost:8000/auth/login/google/callback?code=${code}`,
            { withCredentials: true }
          );

          // Chuyển hướng người dùng
          router.push("/");
        } catch (error) {
          console.error("fail to fetch tokens: ", error);
        }
      }
    };
    fetchTokens();
  }, [code, router]);

  return <div> Đang xử lý đăng nhập...</div>;
};

export default GoogleCallback;
