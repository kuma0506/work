package monotraining;

import java.util.List;
import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import io.sitoolkit.dba.domain.users.UsersEntity;

@Repository
public interface MonoBackRepository extends JpaRepository<UsersEntity, String>{
	List<UsersEntity> findAllByOrderById();
}