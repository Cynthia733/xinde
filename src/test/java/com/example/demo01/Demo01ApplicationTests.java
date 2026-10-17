package com.example.demo01;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

// Skeleton smoke test only: MySQL integration is configured and tested later.
@SpringBootTest(properties = "spring.autoconfigure.exclude=org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration")
class Demo01ApplicationTests {

	@Test
	void contextLoads() {
	}

}
