import { CartType, CartItemType, ActionTypes } from "@/types/types";
import { create } from "zustand";
import { persist } from "zustand/middleware";

const INITIAL_STATE = {
  products: [],
  totalItems: 0,
  totalPrice: 0,
  qrCodeUrl: "",
  lastUpdated: 0,
  email: "",
};

export const useCartStore = create(
  persist<CartType & ActionTypes>(
    (set, get) => ({
      products: INITIAL_STATE.products,
      totalItems: INITIAL_STATE.totalItems,
      totalPrice: INITIAL_STATE.totalPrice,
      qrCodeUrl: INITIAL_STATE.qrCodeUrl,
      lastUpdated: INITIAL_STATE.lastUpdated,
      email: INITIAL_STATE.email,
      addToCart(item: CartItemType) {
        const products = get().products;
        const productInState = products.find(
          (product) => product.id === item.id
        );
        const currentTime = Date.now();
        if (productInState) {
          const updatedProducts = products.map((product) =>
            product.id === productInState.id
              ? {
                  ...product,
                  quantity: product.quantity + item.quantity,
                  price: product.price + item.price,
                }
              : product
          );
          set((state) => ({
            products: updatedProducts,
            totalItems: state.totalItems + item.quantity,
            totalPrice: state.totalPrice + item.price,
            lastUpdated: currentTime,
          }));
        } else {
          set((state) => ({
            products: [...state.products, item],
            totalItems: state.totalItems + item.quantity,
            totalPrice: state.totalPrice + item.price,
            lastUpdated: currentTime,
          }));
        }
      },
      removeFromCart(item: CartItemType) {
        const currentTime = Date.now();
        set((state) => ({
          products: state.products.filter((product) => product.id !== item.id),
          totalItems: state.totalItems - item.quantity,
          totalPrice: state.totalPrice - item.price,
          lastUpdated: currentTime,
        }));
      },
      setQrCodeUrl(url: string) {
        set({ qrCodeUrl: url });
      },
    }),
    { name: "cart", skipHydration: true }
  )
);
