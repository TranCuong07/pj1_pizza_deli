"use client";
import React, { useEffect, useState } from "react";
import Image from "next/image";
import { useCartStore } from "@/utils/store";
import { useRouter } from "next/navigation";
import axios from "axios";
import { toast } from "react-toastify";
import Cookies from "js-cookie";

const CartPage = () => {
  const {
    products,
    totalItems,
    totalPrice,
    setQrCodeUrl,
    removeFromCart,
    lastUpdated,
  } = useCartStore();
  const router = useRouter();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null); // Sửa đổi kiểu của error
  const timestamp = Date.now();
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  useEffect(() => {
    const token = Cookies.get("access_token");
    setIsLoggedIn(!!token);
    console.log(token);
  }, []);

  useEffect(() => {
    useCartStore.persist.rehydrate();
  }, []);

  const handleCheckout = async () => {
    setLoading(true);
    setError(null);
    const cartData = {
      products,
      totalPrice,
      lastUpdated,
    };
    const checkCookie = async () => {
      try {
        const response = await axios.get(
          "http://localhost:8000/order/check-cookie",
          {
            withCredentials: true, // để gửi cookie
          }
        );
        if (response.status === 200) {
          console.log("Cookie được gửi thành công:", response.data);
        } else {
          console.log("Không gửi được cookie.");
        }
      } catch (error) {
        console.error("Lỗi khi gửi cookie:", error);
      }
    };
    checkCookie();

    // try {
    //   if (!isLoggedIn) {
    //     toast.error("Please log in to proceed with the checkout");
    //   } else {
    //     // gui yeu cau tao qr
    //     const response = await axios.post(
    //       `http://localhost:8000/order/qr-code`,
    //       cartData,
    //       {
    //         headers: {
    //           "Content-Type": "application/json",
    //           // Authorization: `Bearer ${token}`, // Thêm JWT vào header
    //         },
    //         withCredentials: true,
    //       }
    //     );
    //     // const rp = await axios.post(
    //     //   `http://localhost:8000/order/qr-code`,
    //     //   cartData,
    //     //   {
    //     //     headers: {
    //     //       "Content-Type": "application/json",
    //     //       // Authorization: `Bearer ${token}`, // Thêm JWT vào header
    //     //     },
    //     //   }
    //     // );

    //     console.log("API Response:", response.data); // Kiểm tra phản hồi từ API
    //     if (response.data.success) {
    //       // console.log("QR Code URL:", response.data.qrCodeUrl); // Kiểm tra giá trị URL QR code
    //       setQrCodeUrl(response.data.qrCodeUrl); // Lưu URL vào store
    //       router.push("/checkout");
    //     } else {
    //       setError("Failed to generate QR code. Please try again.");
    //       toast.error("Failed to generate QR code. Please try again.");
    //     }
    //   }
    // } catch (error: unknown) {
    //   if (axios.isAxiosError(error))
    //     if (error.response && error.response.status === 401) {
    //       toast.error("Please log in to proceed with the checkout.");
    //     } else {
    //       console.error("QR code generation error:", error);
    //       setError("An error occurred. Please try again.");
    //       toast.error("An error occurred. Please try again.");
    //     }
    // } finally {
    //   setLoading(false);
    // }
  };
  return (
    <div className="h-[calc(100vh-6rem)] md:h-[calc(100vh-9rem)] flex flex-col text-red-500 lg:flex-row">
      {/* PRODUCTS CONTAINER */}
      <div className="h-1/2 p-4 flex flex-col justify-center overflow-scroll lg:h-full lg:w-2/3 2xl:w-1/2 lg:px-20 xl:px-40">
        {/* SINGLE ITEM */}
        {products.map((item) => (
          <div className="flex items-center justify-between mb-4" key={item.id}>
            {item.img && (
              <Image src={item.img} alt="" width={100} height={100} />
            )}
            <div className="">
              <h1 className="uppercase text-xl font-bold">
                {item.title}x{item.quantity}
              </h1>
              <span>{item.optionTitle}</span>
            </div>
            <h2 className="font-bold">{item.price}</h2>
            <span
              className="cursor-pointer"
              onClick={() => removeFromCart(item)}
            >
              X
            </span>
          </div>
        ))}
      </div>
      {/* PAYMENT CONTAINER */}
      <div className="h-1/2 p-4 bg-fuchsia-50 flex flex-col gap-4 justify-center lg:h-full lg:w-1/3 2xl:w-1/2 lg:px-20 xl:px-40 2xl:text-xl 2xl:gap-6">
        <div className="flex justify-between">
          <span className="">Subtotal {totalItems}</span>
          <span className="">${totalPrice}</span>
        </div>
        <div className="flex justify-between">
          <span className="">Service Cost</span>
          <span className="">$0.00</span>
        </div>
        <div className="flex justify-between">
          <span className="">Delivery Cost</span>
          <span className="text-green-500">FREE!</span>
        </div>
        <hr className="my-2" />
        <div className="flex justify-between">
          <span className="">TOTAL(INCL. VAT)</span>
          <span className="font-bold">${totalPrice}</span>
        </div>
        <button
          className="bg-red-500 text-white p-3 rounded-md w-1/2 self-end"
          onClick={handleCheckout}
          disabled={loading}
        >
          CHECKOUT
        </button>
      </div>
    </div>
  );
};

export default CartPage;
