package com.example.api.controllers;

import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class TestController {
    @RequestMapping(path = "/test", method = RequestMethod.GET)
    public String test() {
      return "ok from test.";
    }

    @RequestMapping(path = "/test/json", method = RequestMethod.GET)
    public Example testJson() {
      var examplePOJO = new Example();
      examplePOJO.value1 = "foo";
      examplePOJO.value2 = "bar";
      return examplePOJO;
    }

    @RequestMapping(path = "/test/post", method = RequestMethod.POST)
    public Example testPost(@RequestBody Example requestPOJO) {
      requestPOJO.value1 = requestPOJO.value1 + ":AddServer";
      requestPOJO.value2 = requestPOJO.value2 + ":AddServer";
      return requestPOJO;
    }

    // static class で宣言しないと @RequestBody で受け取れない……？
    public static class Example {
  		public String value1;
	  	public String value2;
	  }
}