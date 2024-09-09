export type Category = {
  id: string;
  slug: string;
  title: string;
  desc?: string;
  img?: string;
  color: string;
}[];

export type Product = {
  id: string;
  title: string;
  desc?: string;
  img?: string;
  price: number;
  options?: { title: string; additionalPrice: number }[];
};

export type CartItemType = {
  id: string;
  title: string;
  img?: string;
  price: number;
  optionTitle?: string;
  quantity: number;
};

export type CartType = {
  products: CartItemType[];
  totalItems: number;
  totalPrice: number;
  qrCodeUrl: string;
  lastUpdated: number;
};

export type ActionTypes = {
  addToCart: (item: CartItemType) => void;
  removeFromCart: (item: CartItemType) => void;
  setQrCodeUrl: (url: string) => void;
};

export type OrderType = {
  id: string;
  userEmail: string;
  desc?: string;
  status: string;
  price: number;
  createdAt: Date;
  products: CartItemType[];
};
