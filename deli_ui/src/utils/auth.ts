import { NextAuthOptions, getServerSession } from "next-auth";
import axios from "axios";
import GoogleProvider from "next-auth/providers/google";

export const authOptions: NextAuthOptions = {
  providers: [
    GoogleProvider({
      clientId: process.env.NEXT_PUBLIC_GOOGLE_CLIENT_ID!,
      clientSecret: process.env.NEXT_PUBLIC_GOOGLE_CLIENT_SECRET!,
      authorization: {
        params: {
          redirect_uri: "http://localhost:3000/api/auth/callback/google",
          prompt: "consent",
          access_type: "offline",
          response_type: "code",
        },
      },
      checks: ["none"],
    }),
  ],
  // callbacks: {
  //   async signIn({ account, profile }) {
  //     console.log(account, profile);
  //     return true; // Do different verification for other providers that don't have `email_verified`
  //   },
  // async redirect({ url, baseUrl }) {
  //   // Allows relative callback URLs
  //   if (url.startsWith("/")) return `${baseUrl}${url}`;
  //   // Allows callback URLs on the same origin
  //   else if (new URL(url).origin === baseUrl) return url;
  //   return baseUrl;
  // },
  // },

  // session: {
  //   strategy: "jwt",
  // },
  callbacks: {
    async signIn({ account, profile }) {
      console.log(account, profile);
      // lay thong tin cua user email, full name,...
      // => goi xuong backend => tạo user or đăng nhập => access token (jwt)
      return true; // Do different verification for other providers that don't have `email_verified`
    },
    async jwt({ token, account }) {
      console.log(token, account);
      // if (account && account.provider === "google") {
      //   try {
      //     const response = await axios.post(
      //       `${process.env.NEXT_PUBLIC_BACKEND_URL}/auth/login/google/callback`,
      //       {
      //         code: account.id_token, // Sử dụng `code` từ Google OAuth callback
      //       }
      //     );

      //     const { access_token, refresh_token } = response.data;
      //     token.accessToken = access_token;
      //     token.refreshToken = refresh_token;
      //   } catch (error) {
      //     console.error("Error fetching tokens from backend:", error);
      //   }
      // }
      return token;
    },
    // async session({ session, token }) {
    //   if (
    //     token &&
    //     typeof token.accessToken === "string" &&
    //     typeof token.refreshToken === "string"
    //   ) {
    //     session.user.accessToken = token.accessToken;
    //     session.user.refreshToken = token.refreshToken;
    //   }
    //   return session;
    // },
  },
};

export const getAuthSession = () => getServerSession(authOptions);
