pip3 install -r requirements.txt
pm.test("Successful POST request", function () {
    pm.expect(pm.response.code).to.be.oneOf([200, 201]);
});