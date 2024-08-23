import React from "react";

const Page = () => {
  return (
    <div className="flex flex-col items-center my-5 px-2">
      <div className="w-full max-w-2xl mx-auto">
        {/* Form tạo đơn hàng. Mặc định hiển thị form này khi vào https://123host.asia/sepay/order.php */}
        {/* Form tạo đơn hàng */}
        {/* Hiển thị Giao diện thanh toán (Checkout) khi tạo đơn hàng thành công */}
        <div className="flex flex-col md:flex-row">
          <div className="md:w-2/3">
            <h1 className="flex items-center text-2xl font-bold">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width={48}
                height={48}
                fill="currentColor"
                className="text-green-500"
                viewBox="0 0 16 16"
              >
                <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16" />
                <path d="m10.97 4.97-.02.022-3.473 4.425-2.093-2.094a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-1.071-1.05" />
              </svg>{" "}
              Đặt hàng thành công
            </h1>
            <span className="text-gray-500">Mã đơn hàng #DH210</span>
            <div
              id="success_pay_box"
              className="p-2 text-center pt-3 border-2 border-black mt-5 hidden"
            >
              <h2 className="text-green-500 pt-3 flex items-center justify-center">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width={48}
                  height={48}
                  fill="currentColor"
                  className="text-green-500"
                  viewBox="0 0 16 16"
                >
                  <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14m0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16" />
                  <path d="m10.97 4.97-.02.022-3.473 4.425-2.093-2.094a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-1.071-1.05" />
                </svg>{" "}
                Thanh toán thành công
              </h2>
              <p className="text-center text-green-500 pb-1">
                Chúng tôi đã nhận được thanh toán, đơn hàng sẽ được chuyển đến
                quý khách trong thời gian sớm nhất!
              </p>
            </div>
            <div
              className="flex flex-col md:flex-row mt-5 px-2"
              id="checkout_box"
            >
              <div className="w-full md:w-1/2 text-center my-2 border p-2">
                <p className="font-bold">
                  Cách 1: Mở app ngân hàng và quét mã QR
                </p>
                <div className="my-2">
                  <img
                    src="https://qr.sepay.vn/img?bank=MBBank&acc=0903252427&template=compact&amount=3000&des=DH210"
                    className="w-full"
                  />
                  <div className="text-center mt-2">
                    <a
                      className="btn btn-outline-primary btn-sm"
                      href="https://qr.sepay.vn/img?bank=MBBank&acc=0903252427&template=compact&amount=3000&des=DH210&download=true"
                    >
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width={14}
                        height={14}
                        fill="currentColor"
                        className="inline-block"
                        viewBox="0 0 16 16"
                      >
                        <path d="M.5 9.9a.5.5 0 0 1 .5.5v2.5a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-2.5a.5.5 0 0 1 1 0v2.5a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2v-2.5a.5.5 0 0 1 .5-.5" />
                        <path d="M7.646 11.854a.5.5 0 0 0 .708 0l3-3a.5.5 0 0 0-.708-.708L8.5 10.293V1.5a.5.5 0 0 0-1 0v8.793L5.354 8.146a.5.5 0 1 0-.708.708z" />
                      </svg>{" "}
                      Tải ảnh QR
                    </a>
                  </div>
                  <span className="block mt-2">
                    Trạng thái: Chờ thanh toán...{" "}
                    <div className="spinner-border inline-block" role="status">
                      <span className="sr-only" />
                    </div>
                  </span>
                </div>
              </div>
              <div className="w-full md:w-1/2 text-center border p-2">
                <p className="font-bold">
                  Cách 2: Chuyển khoản thủ công theo thông tin
                </p>
                <div className="text-center">
                  <img
                    src="https://qr.sepay.vn/assets/img/banklogo/MB.png"
                    className="w-full max-h-12 mx-auto"
                  />
                  <p className="font-bold">Ngân hàng MBBank</p>
                </div>
                <table className="table-auto w-full">
                  <tbody>
                    <tr>
                      <td>Chủ tài khoản: </td>
                      <td>
                        <b>Bùi Tấn Việt</b>
                      </td>
                    </tr>
                    <tr>
                      <td>Số TK: </td>
                      <td>
                        <b>0903252427</b>
                      </td>
                    </tr>
                    <tr>
                      <td>Số tiền: </td>
                      <td>
                        <b>3,000đ</b>
                      </td>
                    </tr>
                    <tr>
                      <td>Nội dung CK: </td>
                      <td>
                        <b>DH210</b>
                      </td>
                    </tr>
                  </tbody>
                </table>
                <p className="bg-gray-100 p-2">
                  Lưu ý: Vui lòng giữ nguyên nội dung chuyển khoản DH210 để hệ
                  thống tự động xác nhận thanh toán
                </p>
              </div>
            </div>
          </div>
          <div className="md:w-1/3 bg-gray-100 border-t p-4">
            <p className="font-bold">Thông tin đơn hàng</p>
            <table className="table-auto w-full">
              <tbody>
                <tr>
                  <td>
                    <span className="font-bold">Kem Merino</span>
                  </td>
                  <td className="text-right font-bold">3,000đ</td>
                </tr>
                <tr>
                  <td>Thuế</td>
                  <td className="text-right">-</td>
                </tr>
                <tr>
                  <td>
                    <span className="font-bold">Tổng</span>
                  </td>
                  <td className="text-right font-bold">3,000đ</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
        <div>
          <p className="mt-5">
            <a
              className="text-decoration-none"
              href="https://payment-gateway-demo.sepay.dev/order.php"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width={16}
                height={16}
                fill="currentColor"
                className="inline-block"
                viewBox="0 0 16 16"
              >
                <path
                  fillRule="evenodd"
                  d="M11.354 1.646a.5.5 0 0 1 0 .708L5.707 8l5.647 5.646a.5.5 0 0 1-.708.708l-6-6a.5.5 0 0 1 0-.708l6-6a.5.5 0 0 1 .708 0"
                />
              </svg>{" "}
              Quay lại
            </a>
          </p>
        </div>
        {/* Hiển thị Giao diện thanh toán (Checkout) khi tạo đơn hàng thành công */}
      </div>
    </div>
  );
};

export default Page;
