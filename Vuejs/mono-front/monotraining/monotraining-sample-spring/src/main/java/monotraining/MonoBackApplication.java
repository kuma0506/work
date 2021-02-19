package monotraining;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.domain.EntityScan;
import org.springframework.data.jpa.repository.config.EnableJpaRepositories;

//使用するRepositoryがあるパッケージ
@EnableJpaRepositories("monotraining")
//使用するEntityがあるパッケージ
@EntityScan("io.sitoolkit.dba.domain.users")
@SpringBootApplication
public class MonoBackApplication {

	public static void main(String[] args) {
		SpringApplication.run(MonoBackApplication.class, args);
    }
    
}
