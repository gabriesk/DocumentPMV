-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Table `servidores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `servidores` (
  `id` INT NOT NULL,
  `nome` VARCHAR(60) NOT NULL,
  `setor` VARCHAR(45) NOT NULL,
  `matricula` INT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
COMMENT = '		';

CREATE UNIQUE INDEX `matricula_UNIQUE` ON `servidores` (`matricula` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `transferencias`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `transferencias` (
  `id` BIGINT NOT NULL,
  `mat_remetente` INT NOT NULL,
  `mat_destinatario` INT NOT NULL,
  `assinado` TINYINT NOT NULL,
  `arquivo_endereco` VARCHAR(250) NOT NULL,
  `tipo` ENUM("Definitivo", "Emprestimo") NOT NULL,
  `prazo` DATE NULL,
  `motivo` VARCHAR(256) NOT NULL,
  `data` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `mat_remetente`
    FOREIGN KEY (`mat_remetente`)
    REFERENCES `servidores` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `mat_destinatario`
    FOREIGN KEY (`mat_destinatario`)
    REFERENCES `servidores` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE UNIQUE INDEX `id_UNIQUE` ON `transferencias` (`id` ASC) VISIBLE;

CREATE INDEX `mat_remetente_idx` ON `transferencias` (`mat_remetente` ASC) VISIBLE;

CREATE INDEX `mat_destinatario_idx` ON `transferencias` (`mat_destinatario` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `item_categoria`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `item_categoria` (
  `id` INT NOT NULL,
  `descricao` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `itens`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `itens` (
  `id` BIGINT NOT NULL,
  `categoria` INT NULL,
  `pat_sn` VARCHAR(45) NOT NULL,
  `modelo` VARCHAR(45) NULL,
  `fabricante` VARCHAR(45) NULL,
  `descricao` VARCHAR(256) NULL,
  `itenscol` VARCHAR(45) NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `categoria`
    FOREIGN KEY (`categoria`)
    REFERENCES `item_categoria` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE UNIQUE INDEX `pat_sn_UNIQUE` ON `itens` (`pat_sn` ASC) VISIBLE;

CREATE INDEX `categoria_idx` ON `itens` (`categoria` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `transferencias_itens`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `transferencias_itens` (
  `id_transferencia` BIGINT NULL,
  `id_item` BIGINT NULL,
  CONSTRAINT `id_transferencia`
    FOREIGN KEY (`id_transferencia`)
    REFERENCES `transferencias` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `id_item`
    FOREIGN KEY (`id_item`)
    REFERENCES `itens` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `id_transferencia_idx` ON `transferencias_itens` (`id_transferencia` ASC) VISIBLE;

CREATE INDEX `id_item_idx` ON `transferencias_itens` (`id_item` ASC) VISIBLE;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
