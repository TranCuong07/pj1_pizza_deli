"use client";
import React, { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import { Product } from "@/types/types";
import Link from "next/link";
import Image from "next/image";

const CategoryPage: React.FC = () => {
  const { slug } = useParams(); // Lấy slug từ URL
  const [products, setProducts] = useState<Product[]>([]);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await fetch(
          `http://localhost:8000/category/product_category/${slug}`
        );
        if (response.ok) {
          const data = await response.json();
          setProducts(data);
        } else {
          console.error("Failed to fetch products");
        }
      } catch (error) {
        console.error("Error fetching products:", error);
      }
    };

    fetchProducts();
  }, [slug]);

  return (
    <div className="flex flex-wrap text-red-500">
      {products.length === 0 ? (
        <p>No products found.</p>
      ) : (
        products.map((item) => (
          <Link
            key={item.id}
            className="w-full h-[60vh] border-r-2 border-b-2 border-red-500 sm:w-1/2 lg:w-1/3 p-4 flex flex-col justify-between group odd:bg-fuchsia-50"
            href={`/product/${item.id}`}
          >
            {item.img && (
              <div className="relative h-[80%]">
                <Image src={item.img} alt="" fill className="object-contain" />
              </div>
            )}
            <div className="flex items-center justify-between font-bold">
              <h1 className="text-2xl uppercase p-2">{item.title}</h1>
              <h2 className="group-hover:hidden text-xl">${item.price}</h2>
              <button className="hidden group-hover:block uppercase bg-red-500 text-white p-2 rounded-md">
                Thêm vào giỏ
              </button>
            </div>
          </Link>
        ))
      )}
    </div>
  );
};

export default CategoryPage;
