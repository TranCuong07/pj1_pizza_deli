"use client";
import Price from "@/components/Price";
import { Product } from "@/types/types";
import Image from "next/image";
import { useParams } from "next/navigation";
import React, { useEffect, useState } from "react";

const SingleProductPage: React.FC = () => {
  const { id } = useParams();
  const [singleProduct, setSingleProducts] = useState<Product | null>(null);

  useEffect(() => {
    const fetchProducts_ById = async () => {
      try {
        const response = await fetch(
          `http://localhost:8000/products/products/${id}`
        );
        if (response.ok) {
          const data: Product = await response.json();
          setSingleProducts(data);
        } else {
          console.error("Failed to fetch products");
        }
      } catch (error) {
        console.error("Error fetching products:", error);
      }
    };

    fetchProducts_ById();
  }, [id]);
  if (!singleProduct) {
    return <div>Loading...</div>;
  }

  return (
    <div className="p-4 lg:px-20 xl:px-40 h-screen flex flex-col justify-around text-red-500 md:flex-row md:gap-8 md:items-center">
      {/* IMAGE CONTAINER */}

      {singleProduct.img && (
        <div className="relative w-full h-1/2 md:h-[70%]">
          <Image
            src={singleProduct.img}
            alt=""
            className="object-contain"
            fill
          />
        </div>
      )}
      {/* TEXT CONTAINER */}
      <div className="h-1/2 flex flex-col gap-4 md:h-[70%] md:justify-center md:gap-6 xl:gap-8">
        <h1 className="text-3xl font-bold uppercase xl:text-5xl">
          {singleProduct.title}
        </h1>
        <p>{singleProduct.desc}</p>
        <Price product={singleProduct} />
      </div>
    </div>
  );
};

export default SingleProductPage;
